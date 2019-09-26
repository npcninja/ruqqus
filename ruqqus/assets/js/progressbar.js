// Get score percentage and make width of progress bar

document.addEventListener('DOMContentLoaded', function() {

	var upsNum = +document.getElementById('p-ups').innerHTML;
	var downsNum = +document.getElementById('p-downs').innerHTML;

	var sum = upsNum + downsNum;

	var val = (Math.floor((upsNum / sum) * 100));

	// console log var val for troubleshooting

	console.log(val);

	document.getElementById('score-percent').innerHTML = val + "% upvoted";

	document.getElementById('progressbar').style.width = val + "%";

	// Set background color of progress bar based on score

	if (val = 100) {
		document.getElementById('progressbar').classlist.remove("bg-success");
		document.getElementById('progressbar').classList.add("bg-gold");
	}
	else if (val < 50) {
		document.getElementById('progressbar').classlist.remove("bg-success");
		document.getElementById('progressbar').classList.add("bg-warning");
	};
}, false);
