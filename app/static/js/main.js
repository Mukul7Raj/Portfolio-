// Initialize Three.js scene
let scene, camera, renderer, particles;

function initThreeJS() {
    try {
        // Create scene
        scene = new THREE.Scene();
        
        // Create camera
        camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.z = 5;
        
        // Create renderer
        renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.getElementById('scene-container').appendChild(renderer.domElement);
        
        // Create particles
        const particleCount = 2000;
        const particlesGeometry = new THREE.BufferGeometry();
        const positions = new Float32Array(particleCount * 3);
        
        for (let i = 0; i < particleCount * 3; i += 3) {
            positions[i] = (Math.random() - 0.5) * 10;
            positions[i + 1] = (Math.random() - 0.5) * 10;
            positions[i + 2] = (Math.random() - 0.5) * 10;
        }
        
        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        
        const particlesMaterial = new THREE.PointsMaterial({
            color: 0x0071e3,
            size: 0.02,
            transparent: true,
            opacity: 0.8
        });
        
        particles = new THREE.Points(particlesGeometry, particlesMaterial);
        scene.add(particles);
        
        // Handle window resize
        window.addEventListener('resize', onWindowResize);
        
        // Start animation loop
        animate();
        
        // Hide loading screen after Three.js is initialized
        hideLoadingScreen();
    } catch (error) {
        console.error('Error initializing Three.js:', error);
        hideLoadingScreen();
    }
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
    requestAnimationFrame(animate);
    
    // Rotate particles
    particles.rotation.x += 0.0005;
    particles.rotation.y += 0.0005;
    
    // Update particle positions based on mouse movement
    if (event) {
        const mouseX = (event.clientX / window.innerWidth) * 2 - 1;
        const mouseY = -(event.clientY / window.innerHeight) * 2 + 1;
        
        particles.position.x += mouseX * 0.01;
        particles.position.y += mouseY * 0.01;
    }
    
    renderer.render(scene, camera);
}

// Initialize ScrollMagic
function initScrollMagic() {
    try {
        const controller = new ScrollMagic.Controller();
        
        // Create scene for each project card
        document.querySelectorAll('.project-card').forEach((card, index) => {
            new ScrollMagic.Scene({
                triggerElement: card,
                triggerHook: 0.8,
                reverse: false
            })
            .setClassToggle(card, 'visible')
            .addTo(controller);
        });
    } catch (error) {
        console.error('Error initializing ScrollMagic:', error);
    }
}

// Handle role selection
function initRoleSelection() {
    const roleButtons = document.querySelectorAll('.role-btn');
    const projectCards = document.querySelectorAll('.project-card');
    
    roleButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons
            roleButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            button.classList.add('active');
            
            const selectedRole = button.dataset.role;
            
            // Filter projects
            projectCards.forEach(card => {
                if (selectedRole === 'all' || card.dataset.roles.includes(selectedRole)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}

// Hide loading screen
function hideLoadingScreen() {
    const loadingScreen = document.getElementById('loading-screen');
    if (loadingScreen) {
        loadingScreen.style.opacity = '0';
        setTimeout(() => {
            loadingScreen.style.display = 'none';
        }, 500);
    }
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize Three.js first
    if (typeof THREE !== 'undefined') {
        initThreeJS();
    } else {
        console.error('Three.js not loaded');
        hideLoadingScreen();
    }
    
    // Initialize other features
    if (typeof ScrollMagic !== 'undefined') {
        initScrollMagic();
    }
    
    initRoleSelection();
    
    // Add smooth scrolling to navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
}); 