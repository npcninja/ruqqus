// Get score percentage and make width of progress bar

window.onload = function progressbar() {

	var upsNum = document.getElementById('p-ups').innerHTML;
	var downsNum = document.getElementById('p-downs').innerHTML;

	var val = (upsNum/(upsNum + downsNum))*100

	document.getElementById('progressbar').style.width = val;
}
