// Get score percentage and make width of progress bar

window.onload = function progressbar() {

	pBar = document.getElementById('progressbar');

	scorePercent = document.getElementById('score-percent');

	var upsNum = +document.getElementById('p-ups').innerHTML;
	var downsNum = +document.getElementById('p-downs').innerHTML;

	var sum = upsNum + downsNum;

	var val = (Math.floor((upsNum / sum) * 100));

	console.log(val);

	scorePercent.innerHTML = val + "% upvoted";

	pBar.style.width = val + "%";

	if (val = 100) {
		pBar.classlist.remove("bg-success");
		pBar.classList.add("bg-gold");
	}
	else if (val < 50) {
		pBar.classlist.remove("bg-success");
		pBar.classList.add("bg-warning");
	};
}
