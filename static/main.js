const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
if (isMobile) {
  alert("Can't use in mobile...");
  document.getElementsByTagName('body')[0].innerHTML = "Sorry.. Mobile not supported.."
}