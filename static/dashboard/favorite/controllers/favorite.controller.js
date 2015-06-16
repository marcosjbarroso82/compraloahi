/**
 * FavoriteCtrl
 * @namespace dashBoardApp.favorite.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.favorite.controllers')
        .controller('FavoriteCtrl', FavoriteCtrl);

    FavoriteCtrl.$inject = ['$scope', 'Favorite', 'AlertNotification', 'ngTableParams', '$filter'];

    /**
     * @namespace FavoriteCtrl
     */
    function FavoriteCtrl($scope, Favorite, AlertNotification, ngTableParams, $filter) {
        var vm = this;
        vm.favorites = [];
        $scope.next_page = null;
        $scope.prev_page = null;
        $scope.count_page = 0;
        $scope.current_page = 1;
        $scope.pages = [];


        vm.request = false;
        getFavorites();

        $scope.filters = {
            title: ''
        };

        $scope.tableParams = new ngTableParams({
            page: 1,            // show first page
            count: 10,          // count per page
            filter: $scope.filters,
            sorting: {
                title: 'asc'
            }
        }, {
            total: vm.favorites.length, // length of data
            getData: function($defer, params) {
                // use build-in angular filter
                var filteredData = params.filter() ?
                    $filter('filter')(vm.favorites, params.filter()) :
                    vm.favorites;
                // use build-in angular filter
                var orderedData = params.sorting() ?
                    $filter('orderBy')(filteredData, params.orderBy()) :
                    filteredData;

                params.total(orderedData.length); // set total for recalc pagination
                $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
            }
        });

        function getFavorites(){
            vm.promiseRequest = Favorite.get(function(data) {
                vm.favorites = data.results;
                $scope.next_page = data.next;
                $scope.prev_page = data.previous;
            });




            $scope.$watchCollection("vm.favorites", function () {
                $scope.tableParams.reload();
            });
        }

        $scope.get_favorites_page = function(page){
            vm.promiseRequest = Favorite.get({"page":page},function(response) {
                $scope.current_page = page;
                vm.favorites = response.results;
                $scope.next_page = response.next;
                $scope.prev_page = response.previous;
                vm.request = true;
            }, function(error){

                vm.request = true;
            });
        };

        $scope.remove_favorite = function(favorite){
            var fav = new Favorite({target_object_id: favorite.id});
            fav.$save(function(){
                AlertNotification.info("El aviso " + favorite.title + " fue quitado de tus favoritos");
                vm.favorites.splice(vm.favorites.indexOf(favorite),1);
            });
        }


    }
})();