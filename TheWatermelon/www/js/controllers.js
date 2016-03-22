angular.module('starter.controllers', [])

.controller('Ctrl',function($scope,$http,$state,$location,$ionicLoading,$timeout,$ionicSideMenuDelegate,ApiEndpoint){
            $scope.user={};
            $scope.submit=function(user){
                  
                  $http({
                        method: 'POST',
                        url: ApiEndpoint.url+ 'login/',
                        data:{username:$scope.user.username, password:$scope.user.password}
                      }).then(function successCallback(response) {
                          alert(response.data[0]);
                          console.log("success");
                      }, function errorCallback(response) {
                          console.log("ERROR");
                      });
             $location.url('/Side/dash');
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