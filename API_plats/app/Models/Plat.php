<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use League\Csv\Reader;
use League\Csv\Writer;

class Plat extends Model
{
    use HasFactory;

    public static function all($columns = ['*'])
    {
        $filePath = storage_path('app/plats/plats.csv');
        $csv = Reader::createFromPath($filePath, 'r');
        $csv->setHeaderOffset(0);

        return collect($csv->getRecords());
    }

    // Méthode pour obtenir un plat par son ID
    public static function find($id)
    {
        $filePath = storage_path('app/plats/plats.csv');
        $csv = Reader::createFromPath($filePath, 'r');
        $csv->setHeaderOffset(0);

        foreach ($csv->getRecords() as $record) {
            if ($record['id'] == $id) {
                return $record;
            }
        }

        return null;
    }

    // Méthode pour créer un nouveau plat
    public static function create(array $data)
    {
        $filePath = storage_path('app/plats/plats.csv');
        $csv = Writer::createFromPath($filePath, 'a+'); // 'a+' mode to append data
        $csv->setHeaderOffset(0); // assuming there is a header

        $csv->insertOne($data);
    }

    // Méthode pour mettre à jour un plat existant
    public function updatePlat(array $data)
    {
        $filePath = storage_path('app/plats/plats.csv');
        $csv = Writer::createFromPath($filePath, 'r+');
        $csv->setHeaderOffset(0);

        $records = $csv->getRecords();

        foreach ($records as $index => $record) {
            if ($record['id'] == $this->id) {
                $records[$index] = $data;
                break;
            }
        }

        $csv = Writer::createFromPath($filePath, 'w+');
        $csv->insertAll($records);
    }

    // Méthode pour supprimer un plat
    public function deletePlat()
    {
        $filePath = storage_path('app/plats/plats.csv');
        $csv = Reader::createFromPath($filePath, 'r');
        $csv->setHeaderOffset(0); // assuming there is a header

        $results = collect($csv->getRecords())->reject(function ($record) {
            return $record['id'] == $this->id; // assume you have id as the identifier
        });

        $writer = Writer::createFromPath($filePath, 'w'); // 'w' mode to truncate and rewrite data
        $writer->insertOne($csv->getHeader()); // reinsert header
        $writer->insertAll($results); // reinsert remaining data
    }
}
