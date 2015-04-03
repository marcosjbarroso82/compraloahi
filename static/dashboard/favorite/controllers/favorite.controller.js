/**
 * FavoriteCtrl
 * @namespace dashBoardApp.favorite.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.favorite.controllers')
        .controller('FavoriteCtrl', FavoriteCtrl);

    FavoriteCtrl.$inject = ['$scope', 'Favorite', 'Snackbar'];

    /**
     * @namespace FavoriteCtrl
     */
    function FavoriteCtrl($scope, Favorite, Snackbar) {
        $scope.favorites = {};
        $scope.next_page = null;
        $scope.prev_page = null;
        $scope.count_page = 0;
        $scope.current_page = 1;
        $scope.pages = [];

        getFavorites();


        function getFavorites(){
            Favorite.get(function(data) {
                $scope.favorites = data.results;
                $scope.next_page = data.next;
                $scope.prev_page = data.previous;
            });
        }

        $scope.get_favorites_page = function(page){
            Favorite.get({"page":page},function(response) {
                $scope.current_page = page;
                $scope.favorites = response.results;
                $scope.next_page = response.next;
                $scope.prev_page = response.previous;
            });
        };

        $scope.remove_favorite = function(favorite){
            var fav = new Favorite({target_object_id: favorite.id});
            fav.$save(function(){
                //$scope.favorites.unshift(favorite);
                getFavorites();
            });
        }
    }
})();