var dashBoardControllers = angular.module('dashBoardApp.controllers', []);

dashBoardControllers.controller('UserCtrl', function UserCtrl($scope, User) {
    $scope.users = {};

    Users.query(function(response) {
        $scope.users = response;
    });
});
