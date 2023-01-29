function toggleMobileMenu(menu) {
    menu.classList.toggle('open');
}
$('.count').each(function () {
    $(this).prop('Counter',0).animate({
        Counter: $(this).text()
    }, {
        duration: 5000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
});
const isTouchDevice = 'ontouchstart' in document.documentElement;
disableScroll();
if (!isTouchDevice) smoothScroll();
window.onresize = () => {
  resizeBodyHeight();
};
window.onload = () => {
  enableScroll();
  resizeBodyHeight();
};
// Functions
$('table').DataTable();