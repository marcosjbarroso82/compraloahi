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

