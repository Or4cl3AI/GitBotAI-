// JavaScript code for scripts.js

// Array of section id names
const sections = ["header", "nav-menu", "hero-section", "about-section", "documentation-section", "features-section", "contact-section", "footer"];

// Function to navigate to a specific section
function navigateToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

// Object representing the contact form
const contactForm = document.getElementById('contact-form');

// Function to handle contact form submission
function submitContactForm(event) {
    event.preventDefault();
    const formData = new FormData(contactForm);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });
    // Send formSubmitted message with form data
    window.postMessage({ type: 'formSubmitted', data: data }, '*');
}

// Add event listener to contact form
if (contactForm) {
    contactForm.addEventListener('submit', submitContactForm);
}

// Function to resize the website for mobile view
function resizeForMobile() {
    if (window.innerWidth <= 768) {
        document.body.classList.add('responsive');
    } else {
        document.body.classList.remove('responsive');
    }
}

// Add event listener to window resize event
window.addEventListener('resize', resizeForMobile);

// Call resizeForMobile function on page load
resizeForMobile();
