var dashBoardControllers = angular.module('dashBoardApp.controllers', []);

/*
dashBoardControllers.controller('LocationCtrl', function LocationCtrl($scope, UserLocations) {
    $scope.map = {center: {latitude: -31.4179952, longitude: -64.1890513 }, zoom: 9 };
    $scope.options = {scrollwheel: false};
    $scope.locations = {};
    $scope.location = {};

    $scope.location_options = {
        stroke: {
            color: '#08B21F',
            weight: 2,
            opacity: 1
        },
        fill: {
            color: '#08B21F',
            opacity: 0.5
        },
        geodesic: true, // optional: defaults to false
        draggable: true, // optional: defaults to false
        clickable: true, // optional: defaults to true
        editable: true, // optional: defaults to false
        visible: true, // optional: defaults to true
        radius: 5000
    }


    UserLocations.query(function(response) {
        $scope.locations = response;
    });

    $scope.deleteLocation = function(location, index) {
        $scope.locations[index].$delete(function() {
            $scope.locations.splice(index, 1);
        });
    }

    $scope.doSearch = function(){
        if($scope.location === ''){
            alert('Directive did not update the location property in parent controller.');
            alert('Directive did not update the location property in parent controller.');
        } else {
            console.log($scope.location);
        }
    };

    $scope.addLocation = function() {
        UserLocations.save($scope.location, function(){
            console.log("como paso esto?");
        });
        console.log("addLocation");
        $scope.locations.push($scope.location);
        $scope.location = {};
    };

    $scope.update = function(location){
        location.lat = location.center.latitude;
        location.lng = location.center.longitude;
        console.log("UPDATE FUNCTION");
        UserLocations.update(location, function(){
            window.alert("CAMBIO!");
        });
    };

});
*/
dashBoardControllers.controller('UserCtrl', function UserCtrl($scope, User) {
    $scope.users = {};

    Users.query(function(response) {
        $scope.users = response;
    });
});
