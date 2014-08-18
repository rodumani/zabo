
(function($) {

	var FileHandler = function(element, options) {
		var me = this;
		this.elem = $(element);
		this.options = options;

		this.info = {};
		// init
		this.init();
	};

	FileHandler.prototype = {
		constructor : FileHandler,

		init : function() {
			var me = this;

			for (var i = 0; i < this.options.type_list.length; i++) {
				var plus_button = $(document.createElement('button')).text('+').css({
					'position' : 'relative',
					'height' : '34px',
					'width' : '30px',
					'display' : 'table-cell',
					'vertical-align' : 'middle',
				});
				var typename = this.options.type_list[i].name;
				var input_container = $(document.createElement('div')).addClass('file-' + typename + '-div')
				// override each type option

				plus_button.click(function (type){
					return function (e) {
						e.preventDefault();
						me.appendInput(type);
					};
				}(typename));
				this.info[typename] = $.extend({}, $.fn.file_handler.type_defaults, {
					div : input_container,
					plus : plus_button,
					inputs : [],
				}, this.options.type_list[i]);
				this.elem.append(this.info[typename].div);

				while (this.info[typename].inputs.length < this.info[typename].minimum) {
					this.appendInput(typename);
				}
			}
		},

		updateInputNameAttr : function (type) {
			if (typeof type === "undefined") {
				for (var i = 0; i < this.options.type_list.length; i++) {
					var typename = this.options.type_list[i].name;
					var input_list = this.info[typename].inputs;
					for (var j = 0; j < input_list.length; j++){
						input_list[j].input.attr('name', typename + j);
					}
				}
			} else {

				var input_list = this.info[type].inputs;
				for (var j = 0; j < input_list.length; j++){
					input_list[j].input.attr('name', type + j);
				}
			}
		},

		removeInput : function(type, inputInfo) {

			var index = $.inArray(inputInfo, this.info[type].inputs);
			if (index == -1) {
				return;
			}

			this.info[type].inputs.splice(index, 1);
			var plus = this.info[type].plus.detach();

			var currLen = this.info[type].inputs.length;
			if (this.info[type].minimum >= currLen) {
				$.each(this.info[type].inputs, function(i, v) {
					v.remove.css('visibility', 'hidden');
				});
			} else {
				$.each(this.info[type].inputs, function(i, v) {
					v.remove.css('visibility', 'visible');
				});
			}

			if (currLen < this.info[type].maximum) {
				this.info[type].inputs[currLen-1].div.append(plus);
			} 
			inputInfo.div.remove();
			this.updateInputNameAttr(type);

		},

		appendInput : function (type) {
			var currLen = this.info[type].inputs.length;
			var me = this;

			var inputDiv = $(document.createElement('div')).css(this.info[type].css);

			var input = $(document.createElement('input')).attr('type', 'file').css({
				'margin-right' : '20px'
			});
			var removeButton = $(document.createElement('button')).text('X').css({
				'position' : 'relative',
				'height' : '34px',
				'width' : '30px',
				'display' : 'table-cell',
				'vertical-align' : 'middle',
			});

			inputDiv.append(input).append(removeButton);
			var inputInfo = {
				div : inputDiv,
				input : input,
				remove : removeButton,
			};

			removeButton.click(function(e){
				e.preventDefault();
				me.removeInput(type, inputInfo);
			});

			input.addClass('file-' + type).addClass('form-control');
			this.info[type].div.append(inputDiv);
			this.info[type].inputs.push(inputInfo);

			if (this.info[type].inputs.length < this.info[type].maximum) {
				inputDiv.append(this.info[type].plus.detach());
			} else {
				this.info[type].plus.detach();
			}

			if (this.info[type].minimum >= this.info[type].inputs.length) {
				$.each(this.info[type].inputs, function(i, v) {
					v.remove.css('visibility', 'hidden');
				});
			} else {
				$.each(this.info[type].inputs, function(i, v) {
					v.remove.css('visibility', 'visible');
				});
			}

			this.updateInputNameAttr(type);
		},

	};

	$.fn.file_handler = function(options) {
		var options = $.extend({}, $.fn.file_handler.defaults, options);
		return this.each(function() {
			var $this = $(this);
			var data = $this.data('file-handler');
			if (!data) {
				$this.data('file-handler', (data = new FileHandler(this, options)));
			}
			if (typeof option === 'string') {
				data[option](val);
			}
		});
	}

	$.fn.file_handler.defaults = {
		'show_thumbnail' : false,
		'type_list' : [{
			name : 'main',
		}],
	};

	$.fn.file_handler.type_defaults = {
		minimum : 1,
		maximum : 3,
		default_file : [],
		css : {
			'height' : '33px',
			'margin-bottom' : '15px',
		},
	}

})(window.jQuery);

$(function(){
	var poster_file = $('div#poster-file');
	var file_handler = poster_file.file_handler({
		'show_thumbnail' : true,
		'type_list' : [{
				name : 'main',
				default_file : [],
				minimum : 1,
				maximum : 1,
			},
			{
				name : 'sub',
				default_file : [],
				minimum : 1,
				maximum : 3,
			},]
	}).data('file-handler');

	var start_date = $('#start_date').datepicker({
		dateFormat : 'yy/mm/dd',
		onSelect : function (date, obj) {
			end_date.datepicker('option', 'minDate', date);
		},
	});
	var end_date = $('#end_date').datepicker({
		dateFormat : 'yy/mm/dd',
	});
});
