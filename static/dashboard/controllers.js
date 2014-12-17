var dashBoardControllers = angular.module('dashBoardApp.controllers', []);

dashBoardControllers.controller('AdCtrl', function AdCtrl($scope, Ad) {
    $scope.ads = {};

    Ad.get(function(response) {
        $scope.ads = response.results;
        $scope.count_page = response.count;
        $scope.next_url = response.next;
        $scope.previous_url = response.previous;

    });

    $scope.next = function(){
        console.log("ENTROO AL NEXT");
        console.log($scope.next_url);
        /*
        Ad.my_query($scope.next_url).then(getSuccess);
        function getSucccess(data, headers, status){
            console.log(data);
            $scope.ads = data.results;
        }*/
        Ad.query(function(response) {
            $scope.ads = response.results;
        });
    };

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

dashBoardControllers.controller('UserCtrl', function UserCtrl($scope, User) {
    $scope.users = {};

    Users.query(function(response) {
        $scope.users = response;
    });
});

dashBoardControllers.controller('MessageCtrl', function MessageCtrl($scope, Message) {
    $scope.messages = {};
    $scope.message = {};
    /*
     Message.query(function(response) {
     $scope.messages = response;
     });
     */

    $scope.loadMessages = function(folder){
        Message.getMsgs(folder).then(getSuccess, getError);

        function getSuccess(data){
            $scope.messages = data.data;
        };

        function getError(data){
            console.log('Error al cargar el inbox');
        }
    }

    $scope.delete_bulk = function(){
        var messages = [];
        for(var i=0; i < $scope.messages.length; i++){
            if($scope.messages[i].selected){
                messages.push($scope.messages[i]);
            }
        }

        Message.delete_bulk(messages).then(deleteSuccess, deleteError);

        function deleteSuccess(data, headers, status){
            console.log(data.data);
        }

        function deleteError(data, headers, status){
            console.log(data.data);
        }
    }

    $scope.messages = $scope.loadMessages('inbox');
});

dashBoardControllers.controller('MessageThreadCtrl', function MessageThreadCtrl($scope, Message, $stateParams, $q) {
    $scope.message = {};
    $scope.msgReply = {};

    $scope.loadMessageThread = function(id){
        Message.getMsgThread(id).then(getSuccess, getError);

        function getSuccess(data){
            $scope.message = data.data;
        };

        function getError(data){
            console.log('Error al cargar el mensaje');
        }
    }

    $scope.reply = function(){

        Message.reply($stateParams.id, $scope.msgReply)
            .then(replySuccess, replyError);

        function replySuccess(data){
            console.log('replySuccess');
            console.log(data);
        }

        function replyError(data){
            console.log('replyError');
            console.log("ERROR REPLY" + data);
        }
    }

    console.log($stateParams);
    $scope.message = $scope.loadMessageThread($stateParams.id);
});
