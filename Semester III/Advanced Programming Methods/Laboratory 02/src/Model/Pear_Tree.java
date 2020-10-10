package Model;

public class Pear_Tree implements  Tree{
    private final int age_of_the_tree;
    public Pear_Tree(int age_of_the_tree)
    {
        this.age_of_the_tree=age_of_the_tree;
    }
    @Override
    public int get_age_of_tree()
    {
        return this.age_of_the_tree;
    }
    @Override
    public String toString()
    {
        return "Pear tree with the age: " + age_of_the_tree+" years old\n";
    }
}