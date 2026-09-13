// SWARIYA WEDDINGS — GLOBAL INTERACTIVE SUITE
// Handles Mobile Nav, Contextual WhatsApp Conversion, Pinterest Pinning & "Add to Wedding Brief"

document.addEventListener('DOMContentLoaded', function () {
    // 1. MOBILE NAV TOGGLE
    const toggle = document.querySelector('.nav-toggle');
    const links = document.querySelector('.nav-links');
    if (toggle && links) {
        toggle.addEventListener('click', function () {
            const isOpen = links.classList.toggle('open');
            toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        });

        links.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                links.classList.remove('open');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // 2. CONTEXTUAL DYNAMIC WHATSAPP CONVERSION ENGINE
    initContextualWhatsApp();

    // 3. PINTEREST & WEDDING BRIEF BUILDER HOVER BUTTONS
    initImageActions();
});

function initContextualWhatsApp() {
    let floatingBtn = document.querySelector('.floating-whatsapp-widget');
    if (!floatingBtn) {
        floatingBtn = document.createElement('a');
        floatingBtn.className = 'floating-whatsapp-widget';
        floatingBtn.target = '_blank';
        floatingBtn.rel = 'noopener noreferrer';
        floatingBtn.setAttribute('aria-label', 'Chat with Swariya Lead Planner on WhatsApp');
        
        floatingBtn.innerHTML = `
            <div class="wa-icon-wrap">
                <svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor">
                    <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.664-.699c.971.534 1.776.818 2.796.818 3.182 0 5.768-2.587 5.768-5.768.001-3.18-2.585-5.602-5.768-5.602zm3.394 8.085c-.144.405-.837.774-1.17.824-.312.045-.694.06-2.12-.533-1.498-.621-2.437-2.137-2.512-2.237-.074-.1-2.123-2.825-1.192-3.879.444-.503.974-.537 1.298-.537.112 0 .209.006.299.011.255.011.383.027.551.431.21.503.719 1.758.783 1.888.064.13.107.283.021.454-.085.171-.128.277-.255.426-.128.149-.269.333-.384.448-.128.128-.261.267-.112.523.149.256.662 1.092 1.42 1.767.974.869 1.794 1.139 2.051 1.268.256.128.406.107.555-.064.15-.171.64-.747.811-1.003.171-.256.342-.213.576-.128.235.085 1.494.704 1.75 1.045.256.341.256.639.112 1.044z"/>
                </svg>
            </div>
            <span class="wa-text-label">Ask Swariya</span>
        `;
        document.body.appendChild(floatingBtn);
    }

    const path = window.location.pathname.toLowerCase();
    let customText = "Hi Swariya Weddings! I would like to schedule a discovery call for our upcoming wedding.";

    if (path.includes('/venues/') || path.includes('venue')) {
        const venueH1 = document.querySelector('h1')?.innerText?.replace(/[\n\r]+/g, ' ').trim() || 'a Bengaluru venue';
        customText = `Hi Swariya Weddings, I'm planning a wedding at ${venueH1} and would love to check availability, real costs, and zero-commission vendor options.`;
    } else if (path.includes('calculator')) {
        customText = "Hi Swariya team, I just used your Wedding Budget Calculator on the website and would love to review my estimated breakdown with a planner.";
    } else if (path.includes('cost-guide')) {
        customText = "Hi Swariya team, I'm reviewing your 2026 Bengaluru Wedding Cost Report and would like a customized budget sheet for our guest count.";
    } else if (path.includes('kannada')) {
        customText = "Namaskara Swariya! I am planning a traditional Kannada wedding in Bengaluru and would like to discuss Nandi Pooja, catering, and venue options.";
    } else if (path.includes('telugu')) {
        customText = "Namaste Swariya! I am planning a traditional Telugu wedding in Bengaluru and would like to discuss Pellikuturu, Muhurtham, and venue options.";
    } else if (path.includes('tamil')) {
        customText = "Vanakkam Swariya! I am planning a traditional Tamil wedding in Bengaluru and would like to discuss Oonjal, Muhurtham, and traditional catering.";
    } else if (path.includes('marwari')) {
        customText = "Hi Swariya! I am planning a grand Marwari wedding in Bengaluru and would like to discuss Sangeet, Mayra, and royal venue setups.";
    } else if (path.includes('destination')) {
        customText = "Hi Swariya Weddings! I'm planning a destination wedding in India (Goa / Rajasthan / Kerala / Coorg) and would like to explore venue options, logistics, and transparent estimates.";
    } else if (path.includes('nri')) {
        customText = "Hi Swariya Weddings, I am an NRI living abroad and planning a wedding in India. I would like to set up a virtual walkthrough call.";
    } else if (path.includes('client-portal')) {
        customText = "Hi Swariya Weddings! I'd like to explore the Wedding OS workspace and discuss transparent flat-fee planning for our wedding.";
    } else if (path.includes('brief-builder')) {
        customText = "Hi Swariya! I've created a custom wedding decor moodboard on your brief builder and would like to share it for an estimate.";
    }

    floatingBtn.href = `https://wa.me/918050573382?text=${encodeURIComponent(customText)}`;
}

function initImageActions() {
    const images = document.querySelectorAll('.gallery-grid img, .gallery-item img, .venue-card img, .hero-image img, .portfolio-grid img, .style-card img');
    
    images.forEach(function (img) {
        const wrapper = img.parentElement;
        if (!wrapper || wrapper.classList.contains('pin-wrapper-active')) return;
        
        const computedPos = window.getComputedStyle(wrapper).position;
        if (computedPos === 'static') {
            wrapper.style.position = 'relative';
        }
        wrapper.classList.add('pin-wrapper-active');

        // Action Buttons Overlay Container
        const actionsWrap = document.createElement('div');
        actionsWrap.className = 'image-actions-overlay';

        // 1. Pinterest Button
        const pinBtn = document.createElement('a');
        pinBtn.className = 'pinterest-save-btn';
        pinBtn.target = '_blank';
        pinBtn.rel = 'noopener noreferrer';
        pinBtn.title = 'Save to Pinterest';
        
        const pageUrl = encodeURIComponent(window.location.href);
        const imgUrl = encodeURIComponent(img.src);
        const description = encodeURIComponent((img.alt || document.title) + ' — Luxury Wedding Decor Inspiration by Swariya Weddings Bengaluru');

        pinBtn.href = `https://pinterest.com/pin/create/button/?url=${pageUrl}&media=${imgUrl}&description=${description}`;
        pinBtn.innerHTML = `
            <svg viewBox="0 0 24 24" width="13" height="13" fill="#E60023">
                <path d="M12 0C5.373 0 0 5.372 0 12c0 5.084 3.163 9.426 7.627 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738.098.119.112.224.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.262 7.929-7.262 4.163 0 7.398 2.967 7.398 6.931 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.631-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24 12 24c6.627 0 12-5.373 12-12 0-6.628-5.373-12-12-12z"/>
            </svg>
            <span>Pin</span>
        `;
        actionsWrap.appendChild(pinBtn);

        // 2. Add to Wedding Brief Button
        const briefBtn = document.createElement('button');
        briefBtn.className = 'brief-save-btn';
        briefBtn.type = 'button';
        briefBtn.title = 'Add this decor inspiration to your custom Wedding Brief';
        briefBtn.innerHTML = `✦ Add to Brief`;
        
        briefBtn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            
            // Save to localStorage
            const savedRefs = JSON.parse(localStorage.getItem('swariya_brief_images') || '[]');
            const imageInfo = {
                src: img.src,
                alt: img.alt || 'Swariya Wedding Decor Inspiration',
                url: window.location.href
            };
            
            // Avoid duplicate
            if (!savedRefs.some(item => item.src === imageInfo.src)) {
                savedRefs.push(imageInfo);
                localStorage.setItem('swariya_brief_images', JSON.stringify(savedRefs));
            }

            // Toast feedback
            showToast('✓ Added to your Wedding Brief!', '/wedding-brief-builder.html', 'Open Brief Builder →');
        });
        actionsWrap.appendChild(briefBtn);

        wrapper.appendChild(actionsWrap);
    });
}

function showToast(message, linkUrl, linkText) {
    let toast = document.querySelector('.swariya-toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.className = 'swariya-toast';
        document.body.appendChild(toast);
    }
    toast.innerHTML = `
        <span>${message}</span>
        <a href="${linkUrl}" style="color: #D4AF37; font-weight: 700; margin-left: 10px; text-decoration: underline;">${linkText}</a>
    `;
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 4000);
}
