<?php

namespace App\Http\Controllers;

use App\Models\Plat;
use Illuminate\Http\Request;

class PlatsController extends Controller
{
    public function index()
    {
        $plats = Plat::all();

        return response()->json($plats);
    }

    public function show($id)
    {
        $plat = Plat::find($id);

        if (!$plat) {
            return response()->json(['message' => 'Plat not found'], 404);
        }

        return response()->json($plat);
    }

    public function store(Request $request)
    {
        $data = [
            'id' => rand(),  // Assurez-vous de générer un ID unique ici
            'nom_de_plat' => $request->input('nom_de_plat'),
            'description' => $request->input('description'),
            'categorie' => $request->input('categorie'),
            'prix' => $request->input('prix'),
            'ingredients' => $request->input('ingredients'),
            'allergenes' => $request->input('allergenes'),
            'temps_de_preparation' => $request->input('temps_de_preparation'),
            'temps_de_cuisson' => $request->input('temps_de_cuisson'),
            'disponibilite' => $request->input('disponibilite'),
            'popularite' => $request->input('popularite'),
            'image_url' => $request->input('image_url')
        ];
    
        Plat::create($data);  // Assurez-vous que cette méthode manipule correctement votre fichier CSV
    
        return response()->json($data, 201);
    }

    public function update(Request $request, $id)
    {
        $plat = Plat::find($id);

        if (!$plat) {
            return response()->json(['message' => 'Plat not found'], 404);
        }

        $plat->nom_de_plat = $request->input('nom_de_plat');
        // Update other properties similarly
        $plat->save();

        return response()->json($plat);
    }

    public function destroy($id)
    {
        $plat = Plat::find($id);

        if (!$plat) {
            return response()->json(['message' => 'Plat not found'], 404);
        }
    
        Plat::deletePlat($id);  // Implémentez cette méthode pour manipuler le fichier CSV
    
        return response()->json(['message' => 'Plat deleted']);
    }
}
