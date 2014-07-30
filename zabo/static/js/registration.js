
$.fn.file_handler = function(options) {
	console.log(this);
};

$(function(){
	var poster_file = $('div#poster_file');
	poster_file.file_handler();
});
