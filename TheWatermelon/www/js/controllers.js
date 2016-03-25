angular.module('starter.controllers', [])

.controller('Ctrl',function($scope,$http,$state,$location,$ionicLoading,$timeout,$ionicSideMenuDelegate,ApiEndpoint,$ionicPopup){
            $scope.user = {};
            $scope.submit=function(user){
                 
                  $http({
                        method: 'POST',
                        url: ApiEndpoint.url+ 'login/',
                        data:{username:user.username, password:user.password}
                      }).then(function successCallback(response) {
                          alert(response.data);
                          console.log("success");
						 $scope.showAlert("Logged in successfully!","Logged in");
						  $location.url('/Side/dash');
						  //alert('Logged in');
                      }, function errorCallback(response) {
						  $scope.showAlert("Error during login!","Internal Error");
                         // console.log("ERROR");
						  
                      });
             
			
			}
			$scope.signup = function(user)
			{
				if(user.nam=='' || user.email=='' || user.add == '' || user.pin=='' || user.phone == '' || user.pass == '')
					$scope.showAlert("Some field is empty!","Error");
				else{
				$http({
                        method: 'POST',
                        url: ApiEndpoint.url+ 'signup/',
                        data:{email:user.email, address:user.add, pincode:user.pin, phone:user.phone,password:user.pass}
                      }).then(function successCallback(response) {
                          alert(response.data);
                          //console.log("success");
						  $scope.showAlert("Signed up successfully!","Signed Up");
						  $location.url('/Page1');
						  //alert('Signed up');
						  // $location.url('/Page1');
						  //alert('Signed up');
                      }, function errorCallback(response) {
                          console.log("ERROR");
						  $scope.showAlert("Internal error during login!","Internal error");
						  
                      });
				}
			}
			
			$scope.showAlert = function(msg,head) {
   var alertPopup = $ionicPopup.alert({
     title: head,
     template: msg
	 
			});
$timeout(function() {
     alertPopup.close(); 
  }, 3000);
 			}
      
    /*  if(user.username == 'anusha' && user.password == 'anusha')
      {
      user.username="";
      user.password="";
            $location.url('/Side/home');
      }
      else
      {
      user.username="";
      user.password="";
      alert('Invalid information');}
       */

      $scope.save=function() {
      alert("Saved!");
      $location.url('/Side/dash');
      } 

      $ionicLoading.show({
    content: 'Loading',
    animation: 'fade-in',
    showBackdrop: true,
    maxWidth: 200,
    showDelay: 0
  })

   $timeout(function () {
    $ionicLoading.hide();},1000)

  $scope.toggleLeft = function() {
    $ionicSideMenuDelegate.toggleLeft();
  }

  $scope.signup_redirect = function(){
     $location.url('/signup');
  }
  
            });