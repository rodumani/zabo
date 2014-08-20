
$(function(){

	var start_date = $('#start_date').datepicker({
		dateFormat : 'yy/mm/dd',
		onSelect : function (date, obj) {
			end_date.datepicker('option', 'minDate', date);
		},
	});
	var end_date = $('#end_date').datepicker({
		dateFormat : 'yy/mm/dd',
	});

	var title_counter = $('#registration-title-count');
	var title = $('input#registration-title');
	var title_count = function () {
		var len = title.val().length;
		if (len > 80 ){
			title_counter.css('color', 'red');
		} else {
			title_counter.css('color', 'black');
		}
		title_counter.text(title.val().length + ' / ' + 80);
	};
	title.bind('keydown keyup keypress', title_count);
	title_count();

	$('#registration-category-addon').click(function(e){
		var element = document.getElementById('registration-category-select');
		var event;

		event = document.createEvent('MouseEvents');
		event.initMouseEvent('mousedown', true, true, window);
		element.dispatchEvent(event);
	});

});
