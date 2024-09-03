// Mobile Menu
const mobileMenuOpenIcon = document.querySelector('.mobile-menu-open-icon');
const mobileMenuCloseIcon = document.querySelector('.mobile-menu-close-icon');
const mobileMenu = document.querySelector('.mobile-menu');

function toggleMobileMenu() {
  mobileMenu.classList.toggle('show-menu');
}

mobileMenuOpenIcon.addEventListener('click', toggleMobileMenu);
mobileMenuCloseIcon.addEventListener('click', toggleMobileMenu);

// Pricing
window.onload = function () {
  togglePricing(
    'monthly',
    document.querySelector('.pricing-tab button.active')
  );
};

function togglePricing(planType, button) {
  if (button && button.classList) {
    const buttons = document.querySelectorAll('.pricing-tab button');
    buttons.forEach((btn) => btn.classList.remove('active'));
    button.classList.add('active');

    const pricingItems = document.querySelectorAll('.pricing-item');

    pricingItems.forEach((item) => {
      const monthlyPrice = item.getAttribute('data-monthly-price');
      const yearlyPrice = item.getAttribute('data-yearly-price');
      const spanElement = item.querySelector('h4 span');
      const subElement = item.querySelector('h4 sub');

      if (planType === 'monthly') {
        spanElement.textContent = monthlyPrice;
        subElement.textContent = '/m';
      } else if (planType === 'yearly') {
        spanElement.textContent = yearlyPrice;
        subElement.textContent = '/y';
      }
    });
  }
}
