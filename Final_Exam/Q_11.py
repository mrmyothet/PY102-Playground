"""
PROCEDURE Search(start_node)
    CREATE empty worklist
    ADD start_node TO worklist

    CREATE empty set seen
    ADD start_node TO seen

    WHILE worklist is not empty DO
        current ← GET next item from worklist
        PROCESS current

        FOR EACH neighbor IN neighbors(current) DO
            IF neighbor is NOT in seen THEN
                ADD neighbor TO worklist
                ADD neighbor TO seen
            END IF
        END FOR
    END WHILE
END PROCEDURE
"""
