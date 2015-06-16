/**
 * AdCtrl
 * @namespace dashBoardApp.ad.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.controllers')
        .controller('AdCtrl', AdCtrl);

    AdCtrl.$inject = ['$scope', 'Ad', 'AlertNotification', 'ngTableParams', '$filter'];

    /**
     * @namespace AdCtrl
     */
    function AdCtrl($scope, Ad, AlertNotification, ngTableParams, $filter) {

        var vm = this;

        // Declare functions
        vm.destroy = destroy;

        // Declare vars
        vm.ads = [];

        vm.request = false;

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
            total: vm.ads.length, // length of data
            getData: function($defer, params) {
                // use build-in angular filter
                var filteredData = params.filter() ?
                    $filter('filter')(vm.ads, params.filter()) :
                    vm.ads;
                // use build-in angular filter
                var orderedData = params.sorting() ?
                    $filter('orderBy')(filteredData, params.orderBy()) :
                    filteredData;

                params.total(orderedData.length); // set total for recalc pagination
                $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
            }
        });


        $scope.$watchCollection("vm.ads", function () {
            vm.tableParams.reload();
        });


        function loadAds(page_nro){
            vm.promiseRequest = Ad.getAll().then(getSuccess, getError);

            function getSuccess(data){
                vm.ads = data.data.results;
                vm.request = true;
            }

            function getError(error){
                AlertNotification.error("Error al consultar avisos, vuelva a intentarlo mas tarde");

                vm.request = true;
            }

        }

        init();

        function init(){
            loadAds();
        }

        function destroy(ad) {
            Ad.destroy(ad.id).then(deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                AlertNotification.success("El aviso " + ad.title + " fue eliminado con exito!");
                vm.ads.splice(vm.ads.indexOf(ad),1);
            }

            function deleteError(data, headers, status){
                AlertNotification.error("Error al intentar borrar el aviso");
            }
        }






    }
})();