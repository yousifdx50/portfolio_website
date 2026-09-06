(() => {
    const root = document.documentElement;
    root.classList.add("js");

    const navToggle = document.querySelector(".nav-toggle");
    const navLinks = document.querySelector(".links");
    navToggle?.addEventListener("click", () => {
        const isOpen = navToggle.getAttribute("aria-expanded") === "true";
        navToggle.setAttribute("aria-expanded", String(!isOpen));
        navLinks?.classList.toggle("is-open", !isOpen);
    });
    navLinks?.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            navToggle?.setAttribute("aria-expanded", "false");
            navLinks.classList.remove("is-open");
        });
    });
    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && navLinks?.classList.contains("is-open")) {
            navToggle?.setAttribute("aria-expanded", "false");
            navLinks.classList.remove("is-open");
            navToggle?.focus();
        }
    });

    const filterButtons = document.querySelectorAll(".filter-button");
    const projectCards = document.querySelectorAll(".project-grid .card-project");
    filterButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const filter = button.dataset.filter;
            filterButtons.forEach((item) => {
                const isActive = item === button;
                item.classList.toggle("is-active", isActive);
                item.setAttribute("aria-selected", String(isActive));
            });
            projectCards.forEach((card) => {
                const isVisible = filter === "all" || card.dataset.category === filter;
                card.hidden = !isVisible;
            });
        });
    });

    const inquiryForm = document.querySelector(".inquiry-form");
    inquiryForm?.addEventListener("submit", (event) => {
        event.preventDefault();
        const formData = new FormData(inquiryForm);
        const recipient = inquiryForm.dataset.contactEmail;
        const subject = `${formData.get("project_type")} inquiry from ${formData.get("name")}`;
        const body = [
            `Name: ${formData.get("name")}`,
            `Email: ${formData.get("email")}`,
            `Company: ${formData.get("company") || "Not provided"}`,
            `Project type: ${formData.get("project_type")}`,
            "",
            formData.get("message"),
        ].join("\n");
        const status = inquiryForm.querySelector("[data-form-status]");
        if (!recipient) {
            if (status) status.textContent = "Email contact is not configured yet.";
            return;
        }
        window.location.href = `mailto:${recipient}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    });

    const revealItems = document.querySelectorAll(".reveal");
    if (!revealItems.length) {
        return;
    }

    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches || !("IntersectionObserver" in window)) {
        revealItems.forEach((item) => item.classList.add("is-visible"));
        return;
    }

    const observer = new IntersectionObserver((entries, currentObserver) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) {
                return;
            }
            entry.target.classList.add("is-visible");
            currentObserver.unobserve(entry.target);
        });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });

    revealItems.forEach((item, index) => {
        item.style.setProperty("--reveal-delay", `${Math.min(index * 55, 330)}ms`);
        observer.observe(item);
    });
})();
