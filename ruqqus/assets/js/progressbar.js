// Get score percentage and make width of progress bar

window.onload = function progressbar() {

	var upsNum = document.getElementById('p-ups').innerHTML;
	var downsNum = document.getElementById('p-downs').innerHTML;

	var sum = upsNum + downsNum;

	var div = upsNum/sum;

	var val = div * 1000;

	console.log(val);

	document.getElementById('progressbar').style.width = val + "%";
}
