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

        vm.ads = [];
        $scope.next_page = null;
        $scope.prev_page = null;
        $scope.count_page = 0;
        $scope.current_page = 1;
        $scope.pages = [];

        getAds();


        function getAds(){
            vm.promiseRequest = Ad.get(function(data) {
                vm.ads = data.results;
                $scope.next_page = data.next;
                $scope.prev_page = data.previous;
            });
        }

        $scope.get_ads_page = function(page){
            vm.promiseRequest = Ad.get({"page":page},function(response) {
                $scope.current_page = page;
                vm.ads = response.results;
                $scope.next_page = response.next;
                $scope.prev_page = response.previous;
            });
        };


        $scope.submitAd= function(text) {
            var ad = new Ad({text: text});
            ad.$save(function(){
                vm.ads.unshift(ad);
            })
        };
        $scope.deleteAd= function(ad) {

            Ad.delete({id:ad.id}, deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                AlertNotification.success("El aviso " + ad.title + " fue eliminado con exito!");
                //getAds();
                vm.ads.splice(vm.ads.indexOf(ad),1);

            }

            function deleteError(data, headers, status){
                AlertNotification.error("Error al intentar borrar el aviso");
            }
        };


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
            $scope.tableParams.reload();
        });

    }
})();