from mcp.server.fastmcp import FastMCP


mcp = FastMCP("simple_server", host = "0.0.0.0", port = "10000")

@mcp.tool()
def server_echo(msg: str) -> str:
    """
    Use this tool to echo a message on server

    Args: 
    
        msg: The message in string format.

    Returns:

        task completion status in string format: "successful" if everything goes okay, "failed" if there was a problem.
    """

    try:
        print("Echoing: " + msg)
        return "successful"
    except:
        return "failed"

@mcp.tool()
def server_add_two_ints(arg1: int, arg2: int) -> int:
    """
    Use this tool to add to integer values together

    Args: 
    
        arg1: The first integer value
        arg2: The second integer value

    Returns:

        The result of adding the two values together in integer if the two values are integer
        If there was a problem, or the two values were not integer, returns Null
    """

    try:

        if(type(arg1) == type(arg2) == int):
            res = arg1 + arg2
            return res
        else:
            return None
        
    except:
        return None

if __name__ == "__main__":
    mcp.run(transport="streamable-http")