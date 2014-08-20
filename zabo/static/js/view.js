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
			$("#mainPicture").removeAttr("style");
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
					$("#subPictures").append('<div class="crop"><img src="'+obj.sub_pictures[i].url+'"></div>');
					$(".crop > img").load(function(){
						var height=$(this).height();
						var width=$(this).width();
						if(height<=width){
							$(this).css({"height":"150px","margin-left":(75-width*75/height)+"px"});
						}
						else{
							$(this).css({"width":"150px","margin-top":(75-height*75/width)+"px"});
						}
					});
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

