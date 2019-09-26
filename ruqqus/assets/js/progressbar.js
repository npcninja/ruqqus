// Get score percentage and make width of progress bar

window.onload = function progressbar() {
	var val = document.getElementById('progressbar-value').innerHTML;

	document.getElementById('progressbar').style.width = val;
}
