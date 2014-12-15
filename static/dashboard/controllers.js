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

    $scope.messages = $scope.loadMessages('inbox');
});

dashBoardControllers.controller('MessageThreadCtrl', function MessageThreadCtrl($scope, Message, $stateParams) {
  $scope.message = {};

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
        //var msg = {};
        //msg.body = $scope.body;
        //msg.csrf = $scope.csrfmiddlewaretoken;

        Message.reply($stateParams.id, $scope.msgReply).then(replySuccess, replyError);

        function replySuccess(data){
            console.log(data);
        }

        function replyError(data){
            console.log("ERROR REPLY" + data);
        }
    }


    console.log($stateParams);
    $scope.message = $scope.loadMessageThread($stateParams.id);
});
