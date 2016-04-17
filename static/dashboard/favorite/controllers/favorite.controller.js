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
        vm.request = false;

        vm.remove_favorite = remove_favorite;

        getFavorites();

        vm.filters = {
            title: ''
        };

        vm.tableParams = new ngTableParams({
            page: 1,            // show first page
            count: 10,          // count per page
            filter: vm.filters,
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
            vm.promiseRequest = Favorite.get_favorites().then(getFavoriteSuccess, getFavoriteError);

            function getFavoriteSuccess(data){
                vm.favorites = data.data;
                vm.request = true;
            }

            function getFavoriteError(data){
                vm.request = true;
                AlertNotification.error("Error al intentar traer tus favoritos. Vuelve a intentarlo mas tarde");
            }

            $scope.$watchCollection("vm.favorites", function () {
                vm.tableParams.reload();
            });
        }


        function remove_favorite(favorite){
            vm.promiseRequest = Favorite.toggle_favorites(favorite).then(removeFavoriteSuccess, removeFavoriteError);

            function removeFavoriteSuccess(data){
                AlertNotification.info("El aviso " + favorite.title + " fue quitado de tus favoritos");
                vm.favorites.splice(vm.favorites.indexOf(favorite),1);
            }

            function removeFavoriteError(data){
                AlertNotification.error("Error al intentar quitar el favorito de tu lista, intenta mas tarde");
            }

        }


    }
})();