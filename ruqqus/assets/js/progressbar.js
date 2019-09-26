// Get score percentage and make width of progress bar

window.onload = function progressbar() {

	var upsNum = document.getElementById('p-ups').innerHTML;
	var downsNum = document.getElementById('p-downs').innerHTML;

	var sum = upsNum + downsNum;

	var val = (Math.floor((upsNum / sum) * 1000));

	console.log(val);

	document.getElementById('score-percent').innherHTML = val + "% upvoted";

	document.getElementById('progressbar').style.width = val + "%";
}
