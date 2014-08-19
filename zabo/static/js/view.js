function openModal(article_id){	
	$.ajax({
		type:"GET",
		url:"/board/get_detail/",
		dataType:"json",
		data:{
			article_id : article_id,
		},
		success: function(obj){
			console.log(obj);
			$("#subPictures").empty();
			$("#mainPicture").removeAttr();
			$("#mainPicture").attr("src", obj.main_picture.url);
			$("#mainPicture").removeClass();
			if(obj.sub_pictures.length == 0){
				$("#mainPicture").addClass("largeHeightPicture");
				if($("#mainPicture").width()>=$("#modalPictures").width()*0.9){
					$("#mainPicture").removeClass().addClass("largeWidthPicture");
					$("#mainPicture").css("margin-top",($("#modalPictures").height()-$("#mainPicture").height())/2);
				}
			}
			else{
				for(i=0;i<obj.sub_pictures.length;i++){
					$("#subPictures").append('<img src="'+obj.sub_pictures[i].url+'"class=subPicture>');
				}
			}
			$("#modalTitle").text('['+obj.category+'] '+obj.title);
			$("#modalWriter").text(obj.writer.club_name);
			$("#modalPeriod").text(obj.start_time + ' ~ ' + obj.end_time);
			$("#modalContent").html(obj.comment);
			window.location.href="#modalOpen";
		}
	});
};

