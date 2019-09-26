// Get score percentage and make width of progress bar

window.onload = function() {

	pBar = document.getElementById('progressbar');

	var upsNum = +document.getElementById('p-ups').innerHTML;
	var downsNum = +document.getElementById('p-downs').innerHTML;

	var sum = upsNum + downsNum;

	var val = (Math.floor((upsNum / sum) * 100));

	// console log var val for troubleshooting

	console.log(val);

	document.getElementById('score-percent').innerHTML = val + "% upvoted";

	document.getElementById('progressbar').style.width = val + "%";

	// Set background color of progress bar based on score

	if (val < 50) {
		pBar.classList.remove("bg-success");
		pBar.classList.add("bg-warning");
	}
}
