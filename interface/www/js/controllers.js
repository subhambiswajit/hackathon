var module = angular.module('myIonicApp.controllers');

module.controller('Ctrl',function($scope,$http,$ionicPopup,$state,$location,$ionicLoading,$timeout,$ionicSideMenuDelegate,$rootScope,$log,$ionicScrollDelegate,ContactService){
    //$scope.header = "Welcome to the galaxy's finest smugglers";
    //$scope.smuglers = [];
    
    $scope.submit = function(user){
      $http({
      method: 'POST',
      url: 'http://localhost:8100/api'+ 'smugglers/',
      data: {"username":user.username, "password":user.password}
    }).then(function successCallback(response) {
        $scope.smuglers = [];
        for(var r in response.data) {
          var smugler = response.data[r];
          $scope.smuglers.push(smugler);

        }
        console.log($scope.smuglers);
    }, function errorCallback(response) {
        console.log("ERROR");
    });

    }
        
        /*$scope.getDetails = function(smugler){
        var url = 'http://localhost:8100/api'  + smugler.id+'/';
        $http.get(url).then(function successCallback(response){
            var alertPopup = $ionicPopup.alert({
              title: 'More details',
              template: ''+smugler.name+' '+smugler.lastname+' is a '+response.data+'',
            });
        },function errorCallback(response){
            console.log("ERROR");
        });*/
    }
    )}