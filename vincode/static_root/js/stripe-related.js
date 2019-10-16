  if(sessionStorage.getItem("shouldShow")!='true'){
	$("#back-data").hide()
	$("#info-data").show()
  }

  if(sessionStorage.getItem("shouldShow")==='true'){
	$("#back-data").show()
	$("#info-data").hide()
	sessionStorage.setItem("shouldShow",'false');
  }
  $(document).on("click",'.data-img',function(e){
      let a=$(this).clone()
      $(a).css('width','auto');
      $(a).addClass("rounded img-thumbnail")
      $(".chosen-img").html(a);
  })
   $(document).ready(function(){
	function ajax_call(){
		$.ajax({
			url:"/rest/vincode/",
			method:'GET',
			
		}).then(function(resp){
			let data=resp.results
			var k=0;
			 for(let i=0;i<data.length;i++){
			   if(data[i].vincode_key==	sessionStorage.getItem("value")){
				   k=1;
				   sessionStorage.setItem("id",data[i].id);
				   $("#color").html(data[i].Color)
				   $("#condition").html(data[i].Condition)
				   $("#engine").html(data[i].Engine)
				   $("#make").html(data[i].Make)
				   $("#model").html(data[i].Model)
				   $("#primary_damage").html(data[i].Primary_damage)
				   $("#secondary_damage").html(data[i].Secondary_damage)
				   break;
				  }
			 }
			 if(k==0){
				 $(".text.row").html("");
				 let newDiv=$("<div class='col-12 mt-4'></div>");
				 $(newDiv).html("<h1 class='text-center'>Nəticə tapılmadı</h1>")
				 $(".text.row").html(newDiv);
	
			 }
		})
		 $.ajax({
			url:"/rest/vincode-images/",
			method:'GET',
			
		}).then(function(resp){
			let data=resp.results
			var k=0,check=0;
			 for(let i=0;i<data.length;i++){
	
				 if(data[i].vincode==sessionStorage.getItem("id")){
					 k=1;
					 check=1;
					 if(check==1){
						 console.log("bura esasdir")
						$(".zoom-photo").attr('src',data[i].image);
						check=0;
					}
	
					$(".images-data").append(`<img class='data-img ml-1'  style='display:inline-block' width=190; class='mr-2 rounded img-thumbnail' src=`+data[i].image+`>`)
				  
				}
			 }
			 if(k==0){
				$(".zoom-photo").attr("src",'https://www.hondafsj.com/dist/img/nophoto.jpg');
				$(".zoom-photo").attr("style",'width:100%');}
				sessionStorage.setItem("id",undefined);
		})
	}
	ajax_call()


      $(".search-btn").on("click",function(e){
		  e.preventDefault()
			// ikinci ajax seyfeni yenilenmiyende error vermemesi ucundu
				ajax_call()
		  let value=$(".search-val").val()
		  sessionStorage.setItem("value",value);
		  sessionStorage.setItem("shouldShow",'false');
		   window.location.assign("/billing/")    
      })
    })