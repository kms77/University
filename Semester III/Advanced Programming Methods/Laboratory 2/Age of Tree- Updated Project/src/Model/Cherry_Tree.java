package Model;

public class Cherry_Tree implements Tree{
    private final int age_of_the_tree;
    public Cherry_Tree(int age_of_the_tree)
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
        return "Cherry tree with the age " + age_of_the_tree + " years old\n";
    }
}
