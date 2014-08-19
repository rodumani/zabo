function openModal(article_id){	
	$.ajax({
		type:"GET",
		url:"/board/get_detail/",
		dataType:"json",
		data:{
			article_id : article_id,
		},
		success: function(obj){
			$("#subPictures").empty();
			for(i=0;i<obj.sub_pictures.length;i++){
				$("#subPictures").append('<img src="'+obj.sub_pictures[i]+'"class=subPicture>');
			}
			$("#modalTitle").text(obj.title);
			$("#modalWriter").text(obj.writer_name);
			$("#mainPicture").attr("src", obj.main_picture);
			$("#modalPeriod").text(obj.start_time + ' ~ ' + obj.end_time);
			$("#modalContent").html(obj.content);
			window.location.href="#modalOpen";
		}
	});
};

