$(document).ready(function(){
	$(document).keydown(function(e) {
		switch(e.which) {
			case 27:
				window.location="#modalClose";
				e.preventDefault();
				break;
			default:
				break;
		}
	});
});
