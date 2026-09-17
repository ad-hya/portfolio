document.addEventListener("DOMContentLoaded", function () {
  // Highlight the current page's nav link
  var currentPage = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".navbar-nav .nav-link").forEach(function (link) {
    if (link.getAttribute("href") === currentPage) {
      link.classList.add("active");
    }
  });

  // Scroll reveal: fade + slide up elements as they enter the viewport
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var revealObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("visible");
    });
  }

  // Smooth scroll for same-page anchor links (e.g. "View Projects" -> #projects)
  document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach(function (link) {
    link.addEventListener("click", function (e) {
      var target = document.querySelector(link.getAttribute("href"));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  // Back to top button
  var backToTop = document.getElementById("backToTop");
  if (backToTop) {
    window.addEventListener("scroll", function () {
      backToTop.classList.toggle("show", window.scrollY > 500);
    });
    backToTop.addEventListener("click", function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // Copy email to clipboard with a toast confirmation
  var toast = document.getElementById("toast");
  var toastTimer;
  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toast.classList.remove("show");
    }, 2200);
  }

  document.querySelectorAll('a[href^="mailto:"]').forEach(function (emailLink) {
    emailLink.addEventListener("click", function (e) {
      if (!navigator.clipboard) return;
      var email = emailLink.getAttribute("href").replace("mailto:", "").split("?")[0];
      e.preventDefault();
      navigator.clipboard.writeText(email).then(
        function () {
          showToast("Email copied to clipboard");
        },
        function () {
          window.location.href = emailLink.getAttribute("href");
        }
      );
    });
  });

  // Demo contact form: this site is static (no backend), so we just
  // validate and show a success message instead of submitting anywhere.
  var contactForm = document.getElementById("contactForm");
  if (contactForm) {
    contactForm.addEventListener("submit", function (event) {
      event.preventDefault();
      event.stopPropagation();

      if (!contactForm.checkValidity()) {
        contactForm.classList.add("was-validated");
        return;
      }

      contactForm.classList.add("was-validated");
      var successAlert = document.getElementById("formSuccessAlert");
      successAlert.classList.remove("d-none");
      contactForm.reset();
      contactForm.classList.remove("was-validated");

      setTimeout(function () {
        successAlert.classList.add("d-none");
      }, 5000);
    });
  }
});
