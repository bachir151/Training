import java.util.ArrayList;
import java.util.Random;
import java.lang.Math;

public class proba {


    public static ArrayList<String> table_ascii (){
        ArrayList<String> table = new ArrayList<>();
        for (int i=0; i <95;i++){
            table.add( String.valueOf((char)(32+i)));
        }
        return table;
    }
    
    public static ArrayList<String> password(int longueur_mot_de_passe, int quantité_mot_de_passe){
        Random rand =new Random();
        ArrayList<String> liste_pwd = new ArrayList<>();

        for (int i=0; i<quantité_mot_de_passe;i++){
            String mot_de_passe="";
            for (int j=0; j <longueur_mot_de_passe;j++){
                //concaténation des chaines de caractère  et conversion du int en string
                int lettre=rand.nextInt(126-50)+50;
                mot_de_passe=mot_de_passe+((char)lettre);
            }
            liste_pwd.add(mot_de_passe);

        }
        return liste_pwd;
    }

    public static int occurence(String chaine, ArrayList<String> liste){
        int cpt=0;
        for (String lettre: liste){
            if (lettre.equals(chaine)){
                cpt=cpt+1;
            }
        }
        return cpt;
    }


   public static void main(String[] args) {


      /* ArrayList <String> liste= new ArrayList<>();
       for (Integer i=0; i<11;i++){
           Integer  nombre_suivant=rand.nextInt(10); 
           liste.add(nombre_suivant.toString()); // Conversion Integer en String
       }*/

       ArrayList<String> mots_de_passe=password(6,10);
       System.out.println("Liste des mots de passe générés : " +mots_de_passe);

       System.out.println("Nombre d'occurence = "+ occurence("", mots_de_passe));

       System.out.println(table_ascii());

   }
}