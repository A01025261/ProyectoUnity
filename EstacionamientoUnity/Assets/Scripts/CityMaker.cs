/* Autores:
    Equipo 5
    Alberto Jashua Rodriguez Villegas 	A01752023
    Jeovani Hernandez Bastida 			A01749164
    Maximiliano Benítez Ahumada 		A01752791
    Maximiliano Carrasco Rojas 		    A01025261
 */

using System.Collections;
using System.Collections.Generic;
using UnityEngine;



public class CityMaker : MonoBehaviour
{
    [SerializeField] TextAsset layout;
    [SerializeField] GameObject roadPrefab;
    [SerializeField] GameObject buildingPrefab;
    [SerializeField] GameObject semaphorePrefab;
    [SerializeField] GameObject EspacioLlenoCamioneta;
    [SerializeField] GameObject EspacioLlenoCarro;
    [SerializeField] GameObject EspacioVacio;
    [SerializeField] int tileSize;

    // Start is called before the first frame update
    void Start()
    {
        MakeTiles(layout.text);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void MakeTiles(string tiles)
    {
        int x = 0;
        // Mesa has y 0 at the bottom
        // To draw from the top, find the rows of the file
        // and move down
        // Remove the last enter, and one more to start at 0
        int y = tiles.Split('\n').Length - 1;
        Debug.Log(y);

        Vector3 position;
        GameObject tile;

        for (int i=0; i<tiles.Length; i++) {
            if (tiles[i] == '>' || tiles[i] == '<') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(roadPrefab, position, Quaternion.identity);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'v' || tiles[i] == '^') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(roadPrefab, position, Quaternion.Euler(0, 90, 0));
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 's') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(roadPrefab, position, Quaternion.identity);
                tile.transform.parent = transform;
                tile = Instantiate(semaphorePrefab, position, Quaternion.identity);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'S') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(roadPrefab, position, Quaternion.Euler(0, 90, 0));
                tile.transform.parent = transform;
                tile = Instantiate(semaphorePrefab, position, Quaternion.Euler(0, 90, 0));
                tile.transform.parent = transform;
                x += 1;

                // CAJONES VACÍOS

                //Espacio apuntando hacia abajo.
            }
            else if (tiles[i] == 'I') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioVacio, position, Quaternion.Euler(0, 360, 0));
                tile.transform.parent = transform;
                x += 1;

                //Espacio apuntando hacia arriba.

            }
            else if (tiles[i] == 'K') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioVacio, position, Quaternion.Euler(0, 180, 0));
                tile.transform.parent = transform;
                x += 1;

                //Espacio apuntando hacia la derecha.

            }
            else if (tiles[i] == 'J') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioVacio, position, Quaternion.Euler(0, 270, 0));
                tile.transform.parent = transform;
                x += 1;

                //Espacio apuntando hacia la izquierda.

            }
            else if (tiles[i] == 'L') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioVacio, position, Quaternion.Euler(0, 90, 0));
                tile.transform.parent = transform;
                x += 1;
                // Son los espacios ocupados por una camioneta
            } else if (tiles[i] == 'W') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioLlenoCamioneta, position, Quaternion.Euler(0, 360, 0));
                tile.transform.parent = transform;
                x += 1;
            }   else if (tiles[i] == 'X') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioLlenoCamioneta, position, Quaternion.Euler(0, 180, 0));
                tile.transform.parent = transform;
                x += 1;
            }   else if (tiles[i] == 'A') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioLlenoCamioneta, position, Quaternion.Euler(0, 270, 0));
                tile.transform.parent = transform;
                x += 1;
            }   else if (tiles[i] == 'D') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioLlenoCamioneta, position, Quaternion.Euler(0, 90, 0));
                tile.transform.parent = transform;
                x += 1;

                // CAJONES OCUPADOS POR CARROS

                //Apuntando hacia abajo.
            } else if (tiles[i] == 'T') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioLlenoCarro, position, Quaternion.Euler(0, 360, 0));
                tile.transform.parent = transform;
                x += 1;
                //Apuntando hacia arriba.
            }   else if (tiles[i] == 'G') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioLlenoCarro, position, Quaternion.Euler(0, 180, 0));
                tile.transform.parent = transform;
                x += 1;
                //Apuntando hacia la derecha.
            }   else if (tiles[i] == 'F') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioLlenoCarro, position, Quaternion.Euler(0, 270, 0));
                tile.transform.parent = transform;
                x += 1;
                //Apuntando hacia la izquierda.
            }   else if (tiles[i] == 'H') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(EspacioLlenoCarro, position, Quaternion.Euler(0, 90, 0));
                tile.transform.parent = transform;
                x += 1;
                // Son los espacios donde estan los edificios 
            } else if (tiles[i] == '#'  ) {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(buildingPrefab, position, Quaternion.Euler(0, 90, 0));
                tile.transform.parent = transform;
                x += 1;
                // Son los espacios que indican paredes 
            } else if (tiles[i] == '*') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(buildingPrefab, position, Quaternion.Euler(0, 90, 0));
                tile.GetComponent<Renderer>().materials[0].color = Color.red;
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == '\n') {
                x = 0;
                y -= 1;
            }
        }

    }
}
