<?php

use App\Http\Controllers\PlatsController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});
Route::get('/api/plats', [PlatsController::class, 'index']);
