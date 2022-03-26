$.ajax({
	url: '/getSessionname',
	type: 'GET',
	success: function(response){
		$('#uname').html(response);
	 }
 });