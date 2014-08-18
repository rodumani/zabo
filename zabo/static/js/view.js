function openModal(article_id){	
	$.ajax({
		type:"GET",
		url:"/board/get_detail/",
		data:{
			article_id : article_id,
		},
		success: function(obj){
			alert(obj);
		}
	});
};

