```java
//                                      Task 1

class Person {
  public String name;
  public int id;
  
  public static int personCount = 0;
  
  public Person(String name, int id)
  {
    this.name = name;
    this.id = id;
    personCount ++;
  }
  
  public void details()
  {
    System.out.println("Person Name = " + name + '\n' + "Person ID = " + id);
  }
  
  public static void total_person()
  {
      System.out.println("Total Person so far = " + personCount);
  }
}

public class Main {
    public static void main(String[] args)
    {
      String n = "\n----------------------------------------\n";

      Person habib = new Person("Habib", 1601);
      habib.details();
      Person.total_person();
      habib.total_person(); // object can access static function too!
      
      System.out.println(n);
      
      Person hasib = new Person("Hasib", 1701);
      hasib.details();
      Person.total_person();
      hasib.total_person(); // object can access static function too!
    }
}
```

```java
//                                              Task 2

class Person {
  private String name;
  private int id;
  private static int personCount = 0;
  
  public boolean name_filled = false, id_filled = false;
  
  public void setName(String name)
  {
    this.name = name;
    name_filled = true;
    countThisPerson();
  }
  
  public void setID(int id)
  {
    this.id = id;
    id_filled = true;
    countThisPerson();
  }
  
  public void countThisPerson()
  {
    if(name_filled & id_filled)
    {
      personCount++;
    }
  }
  
  public void details()
  {
    System.out.println("Person Name = " + name + '\n' + "Person ID = " + id);
  }
  
  public static void total_person()
  {
      System.out.println("Total Person so far = " + personCount);
  }
}

public class Main {
    public static void main(String[] args)
    {
      String n = "\n----------------------------------------\n";
      
      Person habib = new Person();
      habib.setName("Habib");
      habib.setID(1601);
      habib.details();
      Person.total_person();
      habib.total_person(); // object can access static function too!
      
      System.out.println(n);
      
      Person hasib = new Person();
      hasib.setName("Hasib");
      hasib.setID(1621);
      hasib.details();
      Person.total_person();
      hasib.total_person(); // object can access static function too!
    }
}
```

```java
//                              Task 3
import java.util.Scanner;

class Person {
  private String name;
  private int id;
  private static int personCount = 0;
  
  public boolean name_filled = false, id_filled = false;
  
  public void setName()
  {
    Scanner input = new Scanner(System.in);
    System.out.println("Input name : ");
    this.name = input.nextLine();
    
    name_filled = true;
    countThisPerson();
  }
  
  public void setID()
  {
    Scanner input = new Scanner(System.in);
    System.out.println("Input ID : ");
    this.id = input.nextInt();
    
    id_filled = true;
    countThisPerson();
  }
  
  public void countThisPerson()
  {
    if(name_filled & id_filled)
    {
      personCount++;
    }
  }
  
  public void details()
  {
    System.out.println("Person Name = " + name + '\n' + "Person ID = " + id);
  }
  
  public static void total_person()
  {
      System.out.println("Total Person so far = " + personCount);
  }
}

public class Main {
    public static void main(String[] args)
    {
      String n = "\n----------------------------------------\n";
      
      Person habib = new Person();
      habib.setName();
      habib.setID();
      habib.details();
      Person.total_person();
      habib.total_person(); // object can access static function too!
      
      System.out.println(n);
      
      Person hasib = new Person();
      hasib.setName();
      hasib.setID();
      hasib.details();
      Person.total_person();
      hasib.total_person(); // object can access static function too!
    }
}
```