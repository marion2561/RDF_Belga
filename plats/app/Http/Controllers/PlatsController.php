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
        $plat = new Plat();
        $plat->nom_de_plat = $request->input('nom_de_plat');
        // Set other properties similarly
        $plat->save();

        return response()->json($plat, 201);
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

        $plat->delete();

        return response()->json(['message' => 'Plat deleted']);
    }
}
