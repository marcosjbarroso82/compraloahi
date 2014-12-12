var dashBoardControllers = angular.module('dashBoardApp.controllers', []);

dashBoardControllers.controller('AdCtrl', function AdCtrl($scope, Ad) {
    $scope.ads = {};

    Ad.query(function(response) {
        $scope.ads = response;
    });

    $scope.submitAd= function(text) {
        var ad = new Ad({text: text});
        ad.$save(function(){
            $scope.ads.unshift(ad);
        })
    }
    $scope.deleteAd= function(ad, index) {
        Ad.delete({id:ad.id}, function(index) {
            $scope.ads.splice(index,1);
        });
    }
});

dashBoardControllers.controller('UserCtrl', function UserCtrl($scope, User) {
    $scope.users = {};

  Users.query(function(response) {
    $scope.users = response;
  });
});

dashBoardControllers.controller('MessageCtrl', function MessageCtrl($scope, Message, $http, $sanitize) {
  $scope.messages = {};
  $scope.unTexto = "este es un Texto";
  $scope.contenido = "contenido original";

  Message.query(function(response) {
    $scope.messages = response;
  });

  $scope.LoadInbox = function(){
      //$scope.contenido = "nuevo contenido del Inbox";
      //console.log("load inbox3");
      $http.get('/message/ajax-inbox/').
        success(function(data, status, headers, config) {
          $scope.contenido = data;
        }).
        error(function(data, status, headers, config) {
          $scope.contenido = "Hubo un error al cargar el Inbox";
      });
  }
  $scope.LoadSent = function(){
      $http.get('/message/ajax-sent/').
        success(function(data, status, headers, config) {
          $scope.contenido = data;
        }).
        error(function(data, status, headers, config) {
          $scope.contenido = "Hubo un error al cargar el Sent";
      });
  }


});
