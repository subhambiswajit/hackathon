angular.module('starter.controllers', [])

.controller('Ctrl',function($scope,$http,$state,$location,$ionicLoading,$timeout,$ionicSideMenuDelegate,ApiEndpoint){
            $scope.user = {};
            $scope.submit=function(user){
                 
                  $http({
                        method: 'POST',
                        url: ApiEndpoint.url+ 'login/',
                        data:{username:$scope.user.username, password:$scope.user.password}
                      }).then(function successCallback(response) {
                          alert(response.data);
                          console.log("success");
						  $location.url('/Side/dash');
						  alert('Logged in');
                      }, function errorCallback(response) {
                          console.log("ERROR");
						  
                      });
             
			
			}
			$scope.signup = function(user)
			{
				
				$http({
                        method: 'POST',
                        url: ApiEndpoint.url+ 'signup/',
                        data:{email:user.email, address:user.add, pincode:user.pin, phone:user.phone,password:user.pass}
                      }).then(function successCallback(response) {
                          alert(response.data);
                          console.log("success");
						  // $location.url('/Page1');
						  alert('Signed up');
                      }, function errorCallback(response) {
                          console.log("ERROR");
						  
                      });
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
  };

  $scope.signup_redirect = function(){
     $location.url('/signup');
  }
  
            });