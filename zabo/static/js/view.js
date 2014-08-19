function openModal(article_id){	
	$.ajax({
		type:"GET",
		url:"/board/get_detail/",
		dataType:"json",
		data:{
			article_id : article_id,
		},
		success: function(obj){
			$("#modalTitle").text(obj.title);
			$("#modalWriter").text(obj.writer_name);
			$("#mainPicture").attr("src", obj.main_picture);
			$("#modalPeriod").text(obj.start_time + ' ~ ' + obj.end_time);
			$("#modalContent").html(obj.content);
			window.location.href="#modalOpen";
		}
	});
};

