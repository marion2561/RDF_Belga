<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PlatsController;

Route::get('/plats', [PlatsController::class, 'index']);
Route::get('/plats/{id}', [PlatsController::class, 'show']); // Obtenir un plat par ID
Route::post('/plats', [PlatsController::class, 'store']); // Créer un nouveau plat
Route::put('/plats/{id}', [PlatsController::class, 'update']); // Mettre à jour un plat existant
Route::delete('/plats/{id}', [PlatsController::class, 'destroy']); // Supprimer un plat
